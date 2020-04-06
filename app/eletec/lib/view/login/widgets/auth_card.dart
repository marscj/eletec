
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

    return container;
  }
  
}