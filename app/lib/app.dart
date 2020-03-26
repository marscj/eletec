import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:google_map_location_picker/generated/i18n.dart'
    as location_picker;

import 'I18n/i18n.dart';
import 'authentication/authentication_bloc.dart';
import 'locale/locale_bloc.dart';
import 'view/home/view.dart';

class EletecApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocBuilder<LocaleBloc, LocaleState>(
      builder: (context, state) {
        return MaterialApp(
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
              primaryColor: Colors.blue,
            ),
            home: BlocProvider<AuthenticationBloc>(
              create: (_) => AuthenticationBloc()..add(AppStarted()),
              child: BlocBuilder<AuthenticationBloc, AuthenticationState>(
                builder: (context, state) {
                  if (state is AuthenticationAuthenticated) {
                    return HomePage();
                  }
                  if (state is AuthenticationUnauthenticated) {
                    // return LoginPage(userRepository: userRepository);
                  }
                  return new Container();
                },
              ),
            ));
      },
    );
  }
}
