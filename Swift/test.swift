In what order does iOS load code?

I have a script called `GeneralHelper.swift` and it looks something like this:

```
// GeneralHelper.swift
let GeneralHelperInstance = GeneralHelper.sharedInstance

public struct GeneralHelper {

    static let sharedInstance = GeneralHelper()

    let coords = Coordinates()

    private init(){}
}
```
and I have `ViewController.swift`:

```
class ViewController: UIViewController{

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override func viewDidAppear(animated: Bool) {
        print(GeneralHelperInstance.coords)
    }

}
```
When does the singleton `GeneralHelperInstance` get created?
```
* Is it created after AppDelegate has fully initialized?
* Is it created before or after ViewController is fully loaded and appeared?
* Is it created asynchronously with ViewController?
```

And, when does it get thrown out of the heap? How does it come back to the heap?
