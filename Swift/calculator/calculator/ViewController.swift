//
//  ViewController.swift
//  calculator
//
//  Created by YOUNG on 3/9/16.
//  Copyright © 2016 Mobile Mob. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var display: UILabel!
    var displayNumber: Int!
    var userIsInTheMiddleOfTypingANumber = false
    var operandStack: [Double] = [0]    // Should include 0 in the beginning
    var operatorStack = [String]()
    var displayTextAsDouble: Double {
        get {
            return NSNumberFormatter().numberFromString(display.text!)!.doubleValue
        } set {
            self.display.text! = "\(newValue)"
            self.userIsInTheMiddleOfTypingANumber = false
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        self.displayNumber = 0
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func appendDigit(sender: UIButton) {
        let digit = sender.currentTitle!
        NSLog("digit \(digit)")
        if self.userIsInTheMiddleOfTypingANumber {
            display.text = display.text! + digit
        } else {
            display.text = digit
            self.userIsInTheMiddleOfTypingANumber = true
        }
    }



    @IBAction func enter() {
        // Enter should always empty the operandStack after
        self.userIsInTheMiddleOfTypingANumber = false

        if self.operandStack.count == 1 && self.operatorStack.count == 1 {
            let n1 = operandStack.removeLast()
            let n2 = self.displayTextAsDouble
            self.runOperation(self.operatorStack.removeLast(), n1: n1, n2: n2)
        } else {
            // Always update the operandStack with display text when not operating
            self.operandStack = [Double]()
            self.operandStack.append(self.displayTextAsDouble)
        }
        NSLog("operandStack = \(operandStack)")

    }

    func runOperation(operatorSign: String, n1:Double, n2:Double) {
        switch operatorSign {
        case "×":
            self.displayTextAsDouble = n1 * n2
        case "−":
            self.displayTextAsDouble = n1 - n2
        case "+":
            self.displayTextAsDouble = n1 + n2
        case "÷":
            self.displayTextAsDouble = n1 / n2
        default: break
        }
        self.operandStack.append(self.displayTextAsDouble)
    }

    @IBAction func operate(sender: UIButton) {
        if self.userIsInTheMiddleOfTypingANumber {
            // A number should be appended to the stack before being calculated
            self.enter()
        }

        let operation = sender.currentTitle!

        if self.operandStack.count >= 2 {
            let last = operandStack.removeLast()
            let first = operandStack.removeLast()
            self.runOperation(operation, n1: first, n2: last)
        } else if self.operandStack.count == 1 {
            self.operatorStack.append(operation)
        }

    }

}
