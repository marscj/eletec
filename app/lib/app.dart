import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:google_map_location_picker/generated/i18n.dart' as location_picker;
import 'locale/app_localization.dart';

class EletecApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Eletec',
      locale: Locale('ar', ''),
      localizationsDelegates: const [
        location_picker.S.delegate,
        S.delegate,
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
      home: Home()
    );
  }
}

class Home extends StatefulWidget {
  
  @override
  State<StatefulWidget> createState() => _HomeState();

}

class _HomeState extends State<Home> {
 
 @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Builder(
        builder: (context) {
          return Center(
            child: Row(children: <Widget>[
              FlatButton(onPressed: () {
                setState(() {
                  S.delegate.load(Locale('en', ''));
                });
              }, child: Text(S.of(context).button)),

              FlatButton(onPressed: () {
                setState(() {
                  S.delegate.load(Locale('ar', ''));
                });
              }, child: Text(S.of(context).button))
            ])
          );
        }
      )
    );
  }
  
}