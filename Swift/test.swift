private var roomsTangoDisplayed = [Room]() {
        willSet {
            /// Remove old floor data
            mapView!.removeAnnotations(roomsTangoDisplayed)
            mapView!.removeAnnotations(roomsTangoDisplayed.map{ room in room.marker! })
        }
        didSet {
            mapView!.addAnnotations(roomsTangoDisplayed)
            let roomMarkers = roomsTangoDisplayed.map{ room in room.marker! }
            if zoomLevelObserver >= MapVCConstants.roomMarkerHideZoomLevel {
                mapView!.addAnnotations(roomMarkers)
            } else {
                hiddenRoomMarkersAsArray = roomMarkers
            }

        }
    }

Aalto TUAS-talo-tango_2.geojson
Aalto TUAS-talo-tango_2.geojson
