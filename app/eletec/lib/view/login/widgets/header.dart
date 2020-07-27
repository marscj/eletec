import 'package:flutter/material.dart';

import '../theme/theme.dart';

class Header extends StatelessWidget {
  Header({
    this.height = 180.0,
    this.offset, 
    this.opacity,
    @required this.loginTheme,
  });

  final double height;
  final Offset offset;
  final double opacity;
  final LoginTheme loginTheme;

  @override
  Widget build(BuildContext context) {

    final Widget logo = Hero(
      tag: 'logo',
      child: Image.asset('assets/images/title.png', color: Colors.amber)
    );
  
    return Container(
      height: height,
      child: FractionalTranslation(
        translation: offset,
        child: Opacity(
          opacity: opacity,
          child: logo,
        )
      )
    );
  }
}