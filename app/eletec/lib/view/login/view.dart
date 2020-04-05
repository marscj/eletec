
import 'package:flutter/material.dart';

import 'theme/theme.dart';

class LoginPage extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}

class LoginView extends StatelessWidget {
  
  @override
  Widget build(BuildContext context) {
    return FlatButton();
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
      // put it here because floatingActionButtonTheme doesnt have highlightColor property
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
