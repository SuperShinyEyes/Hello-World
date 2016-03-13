//
//  CalculatorBrain.swift
//  calculator
//
//  Created by YOUNG on 3/13/16.
//  Copyright © 2016 Mobile Mob. All rights reserved.
//

import Foundation

class CalculatorBrain {
    
    private enum Op: CustomStringConvertible {
        case Operand(Double)
        case UnaryOperation(String, Double -> Double)
        case BinaryOperation(String, (Double, Double) -> Double)
        
        var description: String {
            get {
                switch self {
                case .Operand(let operand):
                    return "\(operand)"
                case .UnaryOperation(let symbol, _):
                    return symbol
                case .BinaryOperation(let symbol, _):
                    return symbol
                }
            }
        }
    }
    
    private var opStack = [Op]()
    
    private var knownOps = Dictionary<String, Op>()
    
    
    init() {
        
        func learnOp(op: Op) {
            knownOps[op.description] = op
        }
        learnOp(Op.BinaryOperation("×", *))
        
        knownOps["×"] = Op.BinaryOperation("×", *)
        knownOps["−"] = Op.BinaryOperation("−", -)
        knownOps["+"] = Op.BinaryOperation("+", +)
        knownOps["÷"] = Op.BinaryOperation("÷", /)
        knownOps["√"] = Op.UnaryOperation("√", sqrt)
    }
    
    private func evaluate(ops: [Op]) -> (result: Double?, remainingOps: [Op]) {
        if !ops.isEmpty {
            // Swift doesn't create a copy until the copy is changed from the original
            // Even if the copy is changed not all is recreated but some copy.
            // Stanford lecture 3. 43:30
            var remainingOps = ops   // Copes ops
            let op = remainingOps.removeLast()
            switch op {
            case .Operand(let operand):
                return (operand, remainingOps)
            case .UnaryOperation(_, let operation):
                let operandEvaluation = self.evaluate(remainingOps)
                if let operand = operandEvaluation.result {
                    return (operation(operand),operandEvaluation.remainingOps)
                }
            case .BinaryOperation(_, let operation):
                let op1Evaluation = self.evaluate(remainingOps)
                if let operand1 = op1Evaluation.result {
                    let op2Evaluation = self.evaluate(op1Evaluation.remainingOps)
                    if let operand2 = op2Evaluation.result {
                        return (operation(operand1, operand2), op2Evaluation.remainingOps)
                    }
                }
            // Don't need 'default' because we covered all possible cases for Op
            }
        }
        return (nil, ops)
    }
    
    func evaluate() -> Double? {
        let (result, _) = self.evaluate(self.opStack)
        return result
//        return self.evaluate(self.opStack).remainingOps
    }
    
    func pushOperand(operand: Double) -> Double? {
        opStack.append(Op.Operand(operand))
        return self.evaluate()
    }
    
    func performOperation(symbol: String) -> Double? {
        // Dictionary always returns optional
        if let operation = self.knownOps[symbol] {
            self.opStack.append(operation)
        }
        return self.evaluate()
    }
}