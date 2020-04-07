
import 'package:flutter/material.dart';
import 'dart:math';

class AuthCard extends StatelessWidget{
  
  const AuthCard({
    Key key, 
    this.angle
  }) : super(key: key);

  final double angle;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final deviceSize = MediaQuery.of(context).size;

    final container =  Container(
      height: deviceSize.height / 2,
      width: deviceSize.width,
      child: Card(

      )
    );

    return Transform( 
      alignment: Alignment.center,
      transform: Matrix4.identity()..setEntry(3, 2, .001)
        ..rotateX(angle),
        // ..scale(angle, angle),
      child: container,
    );
  }
  
}

class LoginCard extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) {
    return null;
  }
  
}