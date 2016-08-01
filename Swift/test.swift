I'm trying to define a class Building which inherits MGLPolygon.
MGLPolygon is defined as:

<!-- language: lang-swift -->

    public class MGLPolygon : MGLMultiPoint, MGLOverlay {

        public var interiorPolygons: [MGLPolygon]? { get }

        public convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count: UInt)

        public convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count: UInt, interiorPolygons: [MGLPolygon]?)
    }

MGLPolygon's designated initializer is hidden in the swift version of SDK. The following would fail.

<!-- language: lang-swift -->

    class Building: MGLPolygon {

        let name: String

        init(name: String, coordinates: [CLLocationCoordinate2D]){
            self.name = name
            super.init(coordinates: &coordinates, count: UInt(coordinates.count))
        }
    }

I checked the [original SDK code](https://github.com/mapbox/mapbox-gl-native/blob/master/platform/darwin/src/MGLPolygon.mm) in Objective-C:

<!-- language: lang-swift -->

    @implementation MGLPolygon

    @dynamic overlayBounds;

    + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count {
        return [self polygonWithCoordinates:coords count:count interiorPolygons:nil];
    }

    + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count interiorPolygons:(NSArray<MGLPolygon *> *)interiorPolygons {
        return [[self alloc] initWithCoordinates:coords count:count interiorPolygons:interiorPolygons];
    }

    - (instancetype)initWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count interiorPolygons:(NSArray<MGLPolygon *> *)interiorPolygons {
        if (self = [super initWithCoordinates:coords count:count]) {
            if (interiorPolygons.count) {
                _interiorPolygons = interiorPolygons;
            }
        }
        return self;
    }

    - (mbgl::LinearRing<double>)ring {
        NSUInteger count = self.pointCount;
        CLLocationCoordinate2D *coordinates = self.coordinates;

        mbgl::LinearRing<double> result;
        result.reserve(self.pointCount);
        for (NSUInteger i = 0; i < count; i++) {
            result.push_back(mbgl::Point<double>(coordinates[i].longitude, coordinates[i].latitude));
        }
        return result;
    }

    - (mbgl::Annotation)annotationObjectWithDelegate:(id <MGLMultiPointDelegate>)delegate {
        mbgl::Polygon<double> geometry;
        geometry.push_back(self.ring);
        for (MGLPolygon *polygon in self.interiorPolygons) {
            geometry.push_back(polygon.ring);
        }

        mbgl::FillAnnotation annotation { geometry };
        annotation.opacity = [delegate alphaForShapeAnnotation:self];
        annotation.outlineColor = [delegate strokeColorForShapeAnnotation:self];
        annotation.color = [delegate fillColorForPolygonAnnotation:self];

        return annotation;
    }

    @end


However, unfortunately I'm not good with Objective-C and I don't understand the code.

## What am I asking?
What is the designated initializer of MGLPolygon in Swift? What does it take as parameters?

## Extra question
Why is the designated initializer hidden?
