import 'package:eletec/locale/locale.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    void onPressed() {
      if (BlocProvider.of<LocaleBloc>(context).state.locale.languageCode ==
          'en') {
        BlocProvider.of<LocaleBloc>(context)
            .add(LocaleUpdate(Locale('ar', '')));
      } else {
        BlocProvider.of<LocaleBloc>(context)
            .add(LocaleUpdate(Locale('en', '')));
      }
    }

    return Scaffold(
      body: Center(
          child: new RaisedButton(
        onPressed: onPressed,
        child: Text('lang'),
      )),
    );
  }
}
