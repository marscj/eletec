import 'package:flutter/material.dart';
import 'package:simple_animations/simple_animations.dart';

class AnimatedBackground extends StatelessWidget {
  
  const AnimatedBackground({
    Key key, 
    @required this.colors,
    this.child,
    this.duration = const Duration(seconds: 3)
  }) : super(key: key);

  final List<Color> colors;
  final Widget child;
  final Duration duration;

  @override
  Widget build(BuildContext context) {
    final tween = MultiTrackTween([
      Track("color1").add(duration, ColorTween(end: Color(0xffD38312), begin: colors[0])),
      Track("color2").add(duration, ColorTween(end: Color(0xffA83279), begin: colors[1]))
    ]);

    return ControlledAnimation(
      playback: Playback.MIRROR,
      tween: tween,
      duration: tween.duration,
      builder: (context, animation) {
        return Container(
          child: child ?? SizedBox.shrink(),
          decoration: BoxDecoration(
              gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [animation["color1"], animation["color2"]])),
        );
      },
    );
  }
}