import 'package:eletec/I18n/i18n.dart';
import 'package:eletec/config/router.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:google_map_location_picker/generated/i18n.dart' as location_picker;

import 'bloc/app_bloc.dart';

class EletecApp extends StatefulWidget {
  
  final AppState state;

  const EletecApp(this.state, {Key key}) : super(key: key);
  
  @override
  State<EletecApp> createState() => EletecAppState(state);
}

class EletecAppState extends State<EletecApp> {

  final AppState state;

  EletecAppState(this.state);

  @override
  Widget build(BuildContext context) => MaterialApp( 
    title: 'Eletec',
    locale: state.locale,
    localizationsDelegates: const [
      location_picker.S.delegate,
      Localization.delegate,
      GlobalMaterialLocalizations.delegate,
      GlobalWidgetsLocalizations.delegate,
      GlobalCupertinoLocalizations.delegate,
    ],
    supportedLocales: const <Locale>[
      Locale('en', ''),
      Locale('ar', ''),
    ],
    theme: ThemeData(
      // primaryColor: Colors.blue,
      primarySwatch: Colors.blue,
      buttonTheme: ButtonThemeData(
        buttonColor: Colors.blue,
        hoverColor: Colors.blue,
        shape: StadiumBorder(),
        textTheme: ButtonTextTheme.primary
      ),
      accentColor: Colors.orange,
      cursorColor: Colors.orange,
      textTheme: TextTheme(
        display2: TextStyle(
          fontFamily: 'OpenSans',
          fontSize: 45.0,
          color: Colors.orange,
        ),
        button: TextStyle(
          fontFamily: 'OpenSans',
        ),
        caption: TextStyle(
          fontFamily: 'NotoSans',
          fontSize: 12.0,
          fontWeight: FontWeight.normal,
          color: Colors.deepPurple[300],
        ),
        display4: TextStyle(fontFamily: 'Quicksand'),
        display3: TextStyle(fontFamily: 'Quicksand'),
        display1: TextStyle(fontFamily: 'Quicksand'),
        headline: TextStyle(fontFamily: 'NotoSans'),
        title: TextStyle(fontFamily: 'NotoSans'),
        subhead: TextStyle(fontFamily: 'NotoSans'),
        body2: TextStyle(fontFamily: 'NotoSans'),
        body1: TextStyle(fontFamily: 'NotoSans'),
        subtitle: TextStyle(fontFamily: 'NotoSans'),
        overline: TextStyle(fontFamily: 'NotoSans'),
      ),
    ),
    onGenerateRoute: Router.instance.generator,
  );
      
}
