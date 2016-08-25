
## Demo 1
I’m trying to find the best way in ios 9 and swift to expand a specific view in my cell when a button in a cell is clicked.
basically I have a button inside a view, and when I click the button the view expands within the cell, pushing the cell down and expanding it too for just that specific cell
```swift
import UIKit
import PlaygroundSupport

@objc class ViewExpander: NSObject {
    var viewToChange: UIView
    var heightConstraint: NSLayoutConstraint

    init(viewToChange: UIView, heightConstraint: NSLayoutConstraint) {
        self.viewToChange = viewToChange
        self.heightConstraint = heightConstraint
    }

    @objc func toggleHeight() {
        if heightConstraint.constant == 100 {
            heightConstraint.constant = 40
        } else {
            heightConstraint.constant = 100
        }

        UIView.animate(withDuration: 0.5, delay: 0, options: [.beginFromCurrentState, .allowUserInteraction], animations: {
            self.viewToChange.layoutIfNeeded()
        }, completion: nil)
    }
}

var demoView = UIView(frame: CGRect(origin: .zero, size: CGSize(width: 400, height: 400)))
demoView.backgroundColor = .lightGray

var wrapperView = UIView(frame: .zero)
wrapperView.backgroundColor = .white
demoView.addSubview(wrapperView)

wrapperView.translatesAutoresizingMaskIntoConstraints = false

var expandingView = UIView(frame: .zero)
expandingView.backgroundColor = UIColor.red.withAlphaComponent(0.6)
expandingView.translatesAutoresizingMaskIntoConstraints = false

var nonExpandingView = UIButton(frame: .zero)
nonExpandingView.backgroundColor = UIColor.yellow.withAlphaComponent(0.6)
nonExpandingView.translatesAutoresizingMaskIntoConstraints = false

wrapperView.addSubview(expandingView)
wrapperView.addSubview(nonExpandingView)

let expandingHeightConstraint = expandingView.heightAnchor.constraint(equalToConstant: 40)

NSLayoutConstraint.activate([

    wrapperView.centerXAnchor.constraint(equalTo: demoView.centerXAnchor),
    wrapperView.centerYAnchor.constraint(equalTo: demoView.centerYAnchor),

    expandingView.topAnchor.constraint(equalTo: wrapperView.topAnchor, constant: 12),
    wrapperView.bottomAnchor.constraint(equalTo: expandingView.bottomAnchor, constant: 12),
    expandingView.leadingAnchor.constraint(equalTo: wrapperView.leadingAnchor),
    expandingView.trailingAnchor.constraint(equalTo: wrapperView.centerXAnchor),
    expandingView.widthAnchor.constraint(equalToConstant: 100),

    nonExpandingView.trailingAnchor.constraint(equalTo: wrapperView.trailingAnchor),
    nonExpandingView.leadingAnchor.constraint(equalTo: wrapperView.centerXAnchor),
    nonExpandingView.centerYAnchor.constraint(equalTo: expandingView.centerYAnchor),
    nonExpandingView.heightAnchor.constraint(equalToConstant: 40),
    nonExpandingView.widthAnchor.constraint(equalToConstant: 100),

    expandingHeightConstraint,
])

let viewExpander = ViewExpander(viewToChange: wrapperView, heightConstraint: expandingHeightConstraint)

nonExpandingView.addTarget(viewExpander, action: #selector(ViewExpander.toggleHeight), for: .touchUpInside)

PlaygroundPage.current.liveView = demoView
```
