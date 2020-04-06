import 'package:flutter/material.dart';

import '../theme/theme.dart';

class Header extends StatelessWidget {
  Header({
    this.title,
    this.height = 250.0,
    @required this.loginTheme,
  });

  final String title;
  final double height;
  final LoginTheme loginTheme;

  @override
  Widget build(BuildContext context) {

    final Widget logo = Hero(
      tag: 'logo',
      child: Image.asset('assets/images/title.png', color: Colors.yellowAccent)
    );
 
    return SizedBox(
      height: height,
      child: AnimatedOpacity(
        opacity: 1.0,
        duration: Duration(milliseconds: 500),
        child: logo,
      ),
    );
  }
}