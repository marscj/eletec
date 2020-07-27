
import 'dart:math';

import 'package:eletec/plugs/flutter_form_builder/flutter_form_builder.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:simple_animations/simple_animations/controlled_animation.dart';
import 'package:simple_animations/simple_animations/multi_track_tween.dart';
import 'package:transformer_page_view/transformer_page_view.dart';

class AuthCard extends StatelessWidget{
  
  const AuthCard({
    Key key, 
    this.angle,
    this.padding = const EdgeInsets.all(0),
    this.alignment = Alignment.center
  }) : super(key: key);

  final double angle;
  final EdgeInsets padding;
  final Alignment alignment;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final deviceSize = MediaQuery.of(context).size;

    final Widget content =  Container(
      width: deviceSize.width,
      height: deviceSize.height,
      padding: padding,
      child: TransformerPageView(
        physics: NeverScrollableScrollPhysics(),
        itemCount: 1,
        index: 0,
        itemBuilder: (context, page) {
          final child = Transform( 
            alignment: Alignment.center,
            transform: Matrix4.identity()..setEntry(3, 2, .001)..rotateX(angle),
            child: LoginCard()
          );
          return Align(
            alignment: alignment,
            child: child,
          );
        },
      ),
    );

    return content;
  }
  
}

class LoginCard extends StatelessWidget {

  const LoginCard({
    Key key, 
    this.scale = 1.0
  }) : super(key: key);
  
  final double scale;

  @override
  Widget build(BuildContext context) {
    
    final deviceSize = MediaQuery.of(context).size;
    final cardWidth = min(deviceSize.width * 0.75, 360.0);
    const cardPadding = 16.0; 

    final tween = MultiTrackTween([
      Track("scale").add(Duration(milliseconds: 400), Tween(begin: 0, end: 1.0), curve: Interval(.4, 1.0, curve: Curves.easeOutBack)),
    ]);
    
    final Widget submitBut = ControlledAnimation(
      playback: Playback.PLAY_FORWARD,
      duration: tween.duration, 
      delay: Duration(milliseconds: 500),
      tween: tween,
      builder: (context, animation) {
        return Container(
          child: Transform.scale(
            scale: animation['scale'],
            child: RaisedButton(
              child: Text('Send'),
              onPressed: (){},
            )
          ),
        );
        // return Container(
        //   width: ss,
        //   child: RaisedButton(
        //     onPressed: () {},
        //     child: Text('data'),
        //   ),
        // );
      },
    );

    final Widget form = FormBuilder(
      child: Container(
        padding: EdgeInsets.only(
          left: cardPadding,
          right: cardPadding,
          top: cardPadding + 10,
        ),
        width: cardWidth,
        child: Column(
          children: <Widget>[
            FormBuilderTextField(
              attribute: 'phone_number',
              decoration: InputDecoration(
                labelText: "Phone",
                prefixIcon: Icon(FontAwesomeIcons.mobileAlt, size: 18,)
              ),
              textInputAction: TextInputAction.next,
              validators: [
                FormBuilderValidators.required(),
                FormBuilderValidators.maxLength(10)
              ],
            ),
            SizedBox(height: 20),
            FormBuilderTextField(
              attribute: 'otp',
              decoration: InputDecoration(
                labelText: "Verify",
                prefixIcon: Icon(FontAwesomeIcons.lock, size: 18,)
              ),
              textInputAction: TextInputAction.done,
              maxLength: 4,
              validators: [
                FormBuilderValidators.required(),
                FormBuilderValidators.maxLength(4)
              ],
            ),
            submitBut,
          ],
        )
      )
    );


    return FittedBox(
      child: Card(
        elevation: 1.0,
        child: form,
      ),
    );
  }
  
}