import 'package:flutter/material.dart';

import 'package:eletec/I18n/i18n.dart';

class SettingPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    void onPressed() {
      
    }

    return Scaffold(
      body: Center(
          child: new RaisedButton(
        onPressed: onPressed,
        child: Text(Localization.of(context).button),
      )),
    );
  }
}
