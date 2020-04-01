import 'package:eletec/authentication/authentication_bloc.dart';
import 'package:eletec/view/ad/bloc/ad_bloc.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'app.dart';
import 'locale/locale_bloc.dart';

void main() {
  runApp(MultiBlocProvider(providers: [
    BlocProvider<AuthenticationBloc>(
      create: (_) => AuthenticationBloc()..add(AppStarted()),
    ),
    BlocProvider<LocaleBloc>(
      create: (_) => LocaleBloc()..add(LocaleInit()),
    ),
    BlocProvider<AdBloc>(
      create: (_) => AdBloc()..add(AdEvent(5)),
    )
  ], child: EletecApp()));
}