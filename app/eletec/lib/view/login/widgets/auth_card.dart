
import 'package:animator/animator.dart';
import 'package:flutter/material.dart';
import 'dart:math';

class AuthCard extends StatefulWidget {

  @override
  State<AuthCard> createState() => _AuthCardState();
}

class _AuthCardState extends State<AuthCard> {
  
  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final deviceSize = MediaQuery.of(context).size;

    final container =  Container(
      height: deviceSize.height,
      width: deviceSize.width,
      child: Center( 
        child: FlutterLogo(
          size: 200, 
          colors: Colors.yellow ,
        )
      )
    );

    return Animator(
      duration: Duration(seconds: 1),
      tweenMap: {
        'rotateZ': Tween<double>(begin: 0.0, end: pi/2),
        'scale': Tween<double>(begin: 1.0, end: .2),
        'size': Tween<double>(begin: 1, end: 1),
        'offset': Tween<Offset>(begin: Offset.zero, end: Offset(2, 0))
      },
      cycles: 5,
      // repeats: 5,   
      builderMap: (anim) => Transform(
        alignment: Alignment.center,
        transform: Matrix4.identity()
          ..rotateY(anim['rotateZ'].value)
          ..scale(anim['scale'].value, anim['scale'].value)
          ..scale(anim['size'].value, anim['size'].value),
        child: container,
      ),
    );
  }
  
}