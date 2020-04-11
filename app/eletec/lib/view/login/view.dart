
import 'dart:math';
import 'package:eletec/view/widgets/widgets.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:simple_animations/simple_animations.dart';

import 'theme/theme.dart';
import 'widgets/widgets.dart';

class LoginPage extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) {
    return LoginView(
      theme: LoginTheme(
        pageColorLight: Colors.blue[400],
        pageColorDark: Colors.indigo,
        buttonTheme: LoginButtonTheme(
          splashColor: Colors.purple,
          backgroundColor: Colors.pinkAccent,
          highlightColor: Colors.lightGreen,
          elevation: 9.0,
          highlightElevation: 6.0,
          shape: BeveledRectangleBorder(
            borderRadius: BorderRadius.circular(10),
          ),
        ),
      ),
    );
  }
}

class LoginView extends StatefulWidget {

  LoginView({
    Key key, 
    this.theme = const LoginTheme(),
  }) : super(key: key) ;

  final LoginTheme theme;

  @override
  State<LoginView> createState() => _LoginViewState();
}

class _LoginViewState extends State<LoginView>{

  @override
  Widget build(BuildContext context) {
    final _theme = _mergeTheme(theme: Theme.of(context), loginTheme: widget.theme);
    final deviceSize = MediaQuery.of(context).size;

    final double headerMargin = 15.0;
    final double cardInitialHeight = 400.0;
    final double cardTopPosition = deviceSize.height / 2 - cardInitialHeight / 2;
    final double headerHeight = cardTopPosition - headerMargin;
 
    final tween = MultiTrackTween([
      Track("offset").add(Duration(milliseconds: 500), Tween<Offset>(begin: Offset(0, -.50), end: Offset(0, .2)), curve: Curves.easeOut),
      Track("opacity").add(Duration(milliseconds: 500), Tween(begin: 0.0, end: 1.0), curve: Curves.easeOut),
      Track("angle").add(Duration(milliseconds: 500), Tween(begin: pi / 2.0, end: 0), curve: Curves.easeOut),
    ]);

    return Scaffold(
      body: Stack(
        children: <Widget>[
          GradientBox(
            colors: [
              widget.theme.pageColorLight,
              widget.theme.pageColorDark
            ],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            child: Align(
              alignment: Alignment.bottomCenter,
              child: Image.asset('assets/images/background.png', colorBlendMode: BlendMode.srcIn, color: Colors.black26)
            )
          ),
          // AnimatedBackground(
          //   duration: Duration(seconds: 5),
          //   colors: [ 
          //     widget.theme.pageColorLight,
          //     widget.theme.pageColorDark
          //   ],
          //   child: Align(
          //     alignment: Alignment.bottomLeft,
          //     child: Image.asset('assets/images/background.png', colorBlendMode: BlendMode.srcIn, color: Colors.black26),
          //   )
          // ),
          SingleChildScrollView(
            child: Theme(
              data: _theme, 
              child: ControlledAnimation( 
                playback: Playback.PLAY_FORWARD,
                duration: tween.duration,
                tween: tween,
                builder: (context, animation) {
                  return Stack( 
                    alignment:Alignment.center,
                    children: <Widget>[
                      Positioned(
                        top: 0,
                        child: Header(
                          height: headerHeight,
                          loginTheme: widget.theme,
                          offset: animation['offset'],
                          opacity: animation['opacity'],
                        ) 
                      ),

                      Positioned(
                        child: AuthCard(
                          alignment: Alignment.topCenter,
                          padding: EdgeInsets.only(top: cardTopPosition),
                          angle: animation['angle'],
                        )
                      ),
                    ]
                  );
                }
              )
            )
          )
        ]
      )
    );
  }
  
  ThemeData _mergeTheme({ThemeData theme, LoginTheme loginTheme}) {
    final originalPrimaryColor = loginTheme.primaryColor ?? theme.primaryColor;
    final primaryDarkShades = getDarkShades(originalPrimaryColor);
    final primaryColor = primaryDarkShades.length == 1
        ? lighten(primaryDarkShades.first)
        : primaryDarkShades.first;
    final primaryColorDark = primaryDarkShades.length >= 3
        ? primaryDarkShades[2]
        : primaryDarkShades.last;
    final accentColor = loginTheme.accentColor ?? theme.accentColor;
    final errorColor = loginTheme.errorColor ?? theme.errorColor;
    // the background is a dark gradient, force to use white text if detect default black text color
    final isDefaultBlackText = theme.textTheme.display2.color ==
        Typography.blackMountainView.display2.color;
    final titleStyle = theme.textTheme.display2
        .copyWith(
          color: loginTheme.accentColor ??
              (isDefaultBlackText
                  ? Colors.white
                  : theme.textTheme.display2.color),
          fontSize: loginTheme.beforeHeroFontSize,
          fontWeight: FontWeight.w300,
        )
        .merge(loginTheme.titleStyle);
    final textStyle = theme.textTheme.body1
        .copyWith(color: Colors.black54)
        .merge(loginTheme.bodyStyle);
    final textFieldStyle = theme.textTheme.subhead
        .copyWith(color: Colors.black.withOpacity(.65), fontSize: 14)
        .merge(loginTheme.textFieldStyle);
    final buttonStyle = theme.textTheme.button
        .copyWith(color: Colors.white)
        .merge(loginTheme.buttonStyle);
    final cardTheme = loginTheme.cardTheme;
    final inputTheme = loginTheme.inputTheme;
    final buttonTheme = loginTheme.buttonTheme;
    final roundBorderRadius = BorderRadius.circular(100);

    return theme.copyWith(
      primaryColor: primaryColor,
      primaryColorDark: primaryColorDark,
      accentColor: accentColor,
      errorColor: errorColor,
      cardTheme: theme.cardTheme.copyWith(
        clipBehavior: cardTheme.clipBehavior,
        color: cardTheme.color ?? theme.cardColor,
        elevation: cardTheme.elevation ?? 12.0,
        margin: cardTheme.margin ?? const EdgeInsets.all(4.0),
        shape: cardTheme.shape ??
            RoundedRectangleBorder(borderRadius: BorderRadius.circular(20.0)),
      ),
      inputDecorationTheme: theme.inputDecorationTheme.copyWith(
        filled: inputTheme.filled,
        fillColor: inputTheme.fillColor ??
            Color.alphaBlend(
              primaryColor.withOpacity(.07),
              Colors.grey.withOpacity(.04),
            ),
        contentPadding: inputTheme.contentPadding ??
            const EdgeInsets.symmetric(vertical: 4.0),
        errorStyle: inputTheme.errorStyle ?? TextStyle(color: errorColor),
        labelStyle: inputTheme.labelStyle,
        enabledBorder: inputTheme.enabledBorder ??
            inputTheme.border ??
            OutlineInputBorder(
              borderSide: BorderSide(color: Colors.transparent),
              borderRadius: roundBorderRadius,
            ),
        focusedBorder: inputTheme.focusedBorder ??
            inputTheme.border ??
            OutlineInputBorder(
              borderSide: BorderSide(color: primaryColor, width: 1.5),
              borderRadius: roundBorderRadius,
            ),
        errorBorder: inputTheme.errorBorder ??
            inputTheme.border ??
            OutlineInputBorder(
              borderSide: BorderSide(color: errorColor),
              borderRadius: roundBorderRadius,
            ),
        focusedErrorBorder: inputTheme.focusedErrorBorder ??
            inputTheme.border ??
            OutlineInputBorder(
              borderSide: BorderSide(color: errorColor, width: 1.5),
              borderRadius: roundBorderRadius,
            ),
        disabledBorder: inputTheme.disabledBorder ?? inputTheme.border,
      ),
      floatingActionButtonTheme: theme.floatingActionButtonTheme.copyWith(
        backgroundColor: buttonTheme?.backgroundColor ?? primaryColor,
        splashColor: buttonTheme.splashColor ?? theme.accentColor,
        elevation: buttonTheme.elevation ?? 4.0,
        highlightElevation: buttonTheme.highlightElevation ?? 2.0,
        shape: buttonTheme.shape ?? StadiumBorder(),
      ),

      highlightColor:
          loginTheme.buttonTheme.highlightColor ?? theme.highlightColor,
      textTheme: theme.textTheme.copyWith(
        display2: titleStyle,
        body1: textStyle,
        subhead: textFieldStyle,
        button: buttonStyle,
      ),
    );
  }
}