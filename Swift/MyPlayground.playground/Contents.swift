//: Playground - noun: a place where people can play

import UIKit


struct DecoratingLayout<
    alias: type, alias2: type where alias.Content == alias2.Content
>: type {}