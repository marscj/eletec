
import 'package:animator/animator.dart';
import 'package:flutter/material.dart';

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
          child: Text('card') 
      )
    );

    return Animator<double>(
      tween: Tween<double>(begin: 0, end: 300),
      cycles: 0,
      builder: (anim) => Center(
        child: Container(
          margin: EdgeInsets.symmetric(vertical: 10),
          height: anim.value,
          width: anim.value,
          child: FlutterLogo(),
        ),
      ),
    );
  }
  
}