## Present Modal VC not from a button
```swift
func performSegueWithIdentifier(identifier: String, sender: AnyObject?) {}
// If you have the VC controller itself(e.g. Alerts or from instantiateViewController)
func presentViewController(viewControllerToPresent: UIViewController, animated flag: Bool, completion: (() -> Void)?) {}
// In horizontally regular environments(iPad), modalPresentationStyle will determine how it appears
.FullScreen
.OverFullScreen // presenter left underneath
.Popover
.FormSheet
// In horizontally compact environments(iPhone), This will adapt to always be full screen!
```

### How to dismiss a view controller
The **presenting** VC is responsible for dismissing. You do this by sending the presenting view controller this message. `func dismissViewControllerAnimated(Bool, completion: () -> Void)` which will dismiss whatever MVC it has presented.

### How is the modal VC animated on the screen?
```swift
var modalTransitionStyle: UIModalTransitionStyle
.CoverVertical  // slides the presented modal VC up from bottom of Screen
.FlipHorizontal
.CrossDissolve
.PartialCurl
```

### Unwind Segue
![Unwind](/images/unwind.png)

The presented MVC will get to `prepareForSegue` as normal
```swift
func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
    if segue.identifier == "Go back unwind Segue" {
      if let unwoundToMVC = segue.destinationViewController as? MyPresentingViewController {
        // prepare unwoundToMVC
      }
    }
}
```

### Popover
![Popover](/images/Popover.png)
* Popovers are not quite the same as other segue-to MVCs.
  * Tab Bar, Split View and Navigation Controllers are UIViewControllers, BUT popovers are not.
* Seguing to a popover is set up the same way though
  * You still ctrl-drag, you still have an identifier, you still get to prepare
* All segues are managed via UIPresentationController
* UIPopoverPresentationController causes the popover to appear

### Popover segue preparation
```swift
func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
    if let identifier segue.identifier {
        switch identifier {
            case "Do sth in a Popover Segue":
                if let vc = segue.destinationViewController as? MyController {
                    if let ppc = vc.popverPresentationController {
                        ppc.permittedArrowDirections = UIPopoverArrowDirection.Any
                        ppc.delegate = self
                    }
                    // more preparation here
                }
            default: break
        }
    }
}
```

### popverPresentationController.delegate
1. Notified popover dismiss
```swift
func popverPresentationControllerDidDismissPopover(ppc: UIPopverPresentationController)
```
2. Adapt to different size classes
```swift
func adaptivePresentationStyleForPresentationController(controller: UIPresentationController, traitCollection: UITraitCollection) -> UIModalPresentationStyle {
    return UIModalPresentationStyle.None // don't adapt
    // default in horizontally compact environments(iPhone) is .FullScreen
}
```
3. Size
    * A popover will be made pretty large unless someone tells it otherwise. The MVC being presented knows best what it's "preferred" size inside a popover would be. It expresses via `var preferredContentSize: CGSize`.

    * The MVC is not guaranteed to be that size, but the system will try its best. You can set or override the var to always return an appropriate size.

4. Embed Segues
    * Putting a VC's  `self.view` in another VC's view hierarchy
    * Drag out a `Container View` from the object palette into the scene you want to embed it in. Automatically sets up an "Embed Segue" from container VC to the contained VC.

## Core Location `CLLocation`
* Properties:
    * `coordinate`
    * `altitude`
    * `horizontal/verticalAccuracy`
    * `timestamp`
    * `speed`
    * `course`

#### Where?
```swift
var coordinate: CLLocationCoordinate2D
struct CLLocationCoordinate2D {
    CLLocationDegrees latitude   // Double
    CLLocationDegrees longitude  // Double
}

var altitude: CLLocationDistance // meters. negative means sea level
```
#### Accuracy?
```swift
var horizontalAccuracy: CLLocationAccuracy  // in meters
var verticalAccuracy: CLLocationAccuracy  // in meters
// A negative value means the coordinate or altitude(respectively) is invalid

kCLLocationAccuracyBestForNavigation
kCLLocationAccuracyBest
kCLLocationAccuracyNearestTenMeters
kCLLocationAccuracyHundredMeters
kCLLocationAccuracyKilometer
kCLLocationAccuracyThreeKilometers
```
#### Speed
```swift
var speed: CLLocationSpeed   // meters/sec
// Instantaneous speed. Negative value means "speed is invalid"

```
#### Course
```swift
var course: CLLocationDirection   // degrees, 0 is north, clockwise
// Not all device delivers this. Negative value means "speed is invalid"

```
#### Time stamp
```swift
var timestamp: NSDate
// pay attention to these since locations will be delivered on an inconsistent time basis
```
#### Asking CLLocationManager what your hardware can do
```swift
// Authorized, Denied or Restricted
class func authorizationStatus() -> CLAuthorizationStatus{}
//user enabled (or not) locations for your app
class func locationServicesEnabled() -> Bool {}
class func significantLocationChangeMonitoringAvailable() -> Bool{}
// CLBeacon / CLCircularRegion
class func isMonitoringAvailableForClass(AnyClass!) -> Bool{}
// device can tell how far it is from beacons
class func isRangingAvailable() -> Bool{}
```
#### Asking the user if you can monitor their location
```swift
func requestWhenInUseAuthorization(){}  // only when active
func requestAlwaysAuthorization(){}     // Always
// These obtain authorization from the user asynchronously.
// You can find out when authorization has been granted via a delegate method.
// Until granted, authorizationStatus will be NotDetermined
authorizationStatus.NotDetermined
```
#### ADD Info.plist entry
* NSLocationWhenInUseUsageDescription
* NSLocationAlwaysUsageDescription

#### Accuracy-based continuous location monitoring
```swift
var desiredAccuracy: CLLocationAccuracy // always set this as low as will work for you
// Can also limit updates to only occurring if the change in location exceeds a certain distance
var distanceFilter: CLLocationAccuracy
```
#### Starting and stopping normal position monitoring
```swift
func startUpdatingLocation(){}
func stopUpdatingLocation(){}
// TURN UPDATING OFF when your app is not going to consume the changes.
```
#### Get notified via the CLLocationManager's delegate
```swift
func locationManager(CLLocationManager, didUpdateLocations: [CLLocation])
```
#### Similar API for heading (`CLHeading`, et.al.)
#### Error reporting to the delegate
```swift
func locationManager(CLLocationManager, didFailWithError: NSError)

// Not always a fatal thing, so pay attention to this delegate method
kCLErrorLocationUnknown // Likely temporary, keep waiting (for a while at least)
kCLErrorDenied          // User refused to allow your application to receive updates
kCLErrorHeadingFailure  // Too much local magnetic interference, keep waiting
```
#### Significant location change monitoring in CLLocationManager (vehicles)
```swift
func startMonitoringSiginificantLocationChanges(){}
func stopMonitoringSiginificantLocationChanges(){}
// TURN UPDATING OFF when not needed
```
* This works even if your application **is not running / in background**
* `func application(UIApplication, didFinishLaunchingWithOptions: [NSObject:AnyObject])` will have a dictionary entry for `UIApplicationLaunchOptionsLocationKey`.
* Create a CLLocationManager, then get the latest location via `var location: CLLocation`
* If running in background, **don't take too long**(a few seconds)!

#### Region-based location monitoring in CLLocationManager
```swift
func startMonitoringForRegion(CLRegion){} // CLCircularRegion/CLBeaconRegion
func stopMonitoringForRegion(CLRegion){}
let cr = CLCircularRegion(center: CLLocationCoordinate2D,
                            radius: CLLocationDistance,
                            identifier: String)  // to monitor an area
// CLBeaconRegion is for detecting when you are near another device.
```

#### Get notified via the CLLocationManager's delegate
```swift
func locationManager(CLLocationManager, didEnterRegion: CLRegion)
func locationManager(CLLocationManager, didExitRegion: CLRegion)
func locationManager(CLLocationManager, monitoringDidFailForRegion: CLRegion, withError: NSError)
```

#### Region-monigoring also works if your app is not running
```swift
var monitoredRegions: Set<CLRegion>  // this is a property in CLLocationManager
```
#### CLRegions are tracked by name
Because they survive app termination/relaunch

#### Circular region monitoring size limit
```swift
var maximumRegionMonitoringDistance: CLLocationDistance { get }
```
Attempting to monitor a region larger than this(radius in meters) will generate an error.
Negative value means the region monitoring is not working

#### Beacon regions can also detect range from a beacon
```swift
func startRangingBeaconsInRegion(CLBeaconRegion)
// Delegate method
func locationManager(didRangeBeacons:inRegion:)
// gives you CLBeacon objects and they will tell you proximity
CLProximityImmediate/Near/Far
```

#### To be a beacon is a bit more involved
* Beacons are identified by a globally unique UUID(you generate)
* Check out CBPeripheralManager (Core Bluetooth Framework)


## MapKit
`MKMapView` displays a map
```swift
import MapKit
let mapView = MKMapView()
var annotations: [MKAnnotation] {get}  // MKAnnotation is a protocol
```

#### How are MKAnnotationViews created & associated with annotations?
```swift
func mapView(sender: MKMapView, viewForAnnotation: MKAnnotation) -> MKAnnotationView {
    var view: MKAnnotationView! = sender.dequeueReusableAnnotationViewWithIdentifier(IDENT)
    if view == nil {
        view = MKPinAnnotationView(annotation: annotation, reuseIdentifier: IDENT)
        view.canShowCallout = true // or false
    }
    view.annotation = annotation  // this happens twice if no dequeue
    // prepare and (if not too expensive) load up accessory views here
    // or reset them and wait until mapView(didSelectAnnotationView:) to load actual data
    return view
}
```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```

####
```swift

```
