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
```swift
```

## Core Location `CLLocation`
* Properties:
    * `coordinate`
    * `altitude`
    * `horizontal/verticalAccuracy`
    * `timestamp`
    * `speed`
    * `course`
* Where?
```swift
var coordinate: CLLocationCoordinate2D
struct CLLocationCoordinate2D {
    CLLocationDegrees latitude   // Double
    CLLocationDegrees longitude  // Double
}

var altitude: CLLocationDistance // meters. negative means sea level
```
* Accuracy?
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

##

```swift
```

##

```swift
```

##

```swift
```

##

```swift
```

##

```swift
```
