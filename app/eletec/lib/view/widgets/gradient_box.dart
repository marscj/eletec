import 'package:flutter/material.dart';

class GradientBox extends StatelessWidget {
  GradientBox({
    this.colors,
    this.begin = Alignment.topLeft,
    this.end = Alignment.bottomRight,
    this.child
  });

  final AlignmentGeometry begin;
  final AlignmentGeometry end;
  final List<Color> colors;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: child ?? SizedBox.expand(),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: colors ?? [
            Theme.of(context).primaryColor,
            Theme.of(context).primaryColorDark,
          ],
          begin: begin,
          end: end,
          stops: [0.0, 1.0],
        ),
      ),
    );
  }
}
