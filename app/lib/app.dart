import 'package:flutter/material.dart';
import 'package:bloc/bloc.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:google_map_location_picker/generated/i18n.dart'
    as location_picker;

import 'authentication/authentication.dart';
import 'locale/localization.dart' as S;
import 'view/home/view.dart';

class EletecApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocBuilder(
        listeners: [
          BlocListener<AuthenticationBloc, AuthenticationState>(
            listener: (_, __) {},
          )
        ],
        child: MaterialApp(
            title: 'Eletec',
            locale: Locale('ar', ''),
            localizationsDelegates: const [
              location_picker.S.delegate,
              S.Localization.delegate,
              GlobalMaterialLocalizations.delegate,
              GlobalWidgetsLocalizations.delegate,
              GlobalCupertinoLocalizations.delegate,
            ],
            supportedLocales: const <Locale>[
              Locale('en', ''),
              Locale('ar', ''),
            ],
            theme: ThemeData(
              primaryColor: Colors.blue,
            ),
            home: HomePage()));
  }
}
