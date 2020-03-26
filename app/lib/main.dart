import 'package:eletec/view/ad/bloc/ad_bloc.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'app.dart';
import 'locale/locale_bloc.dart';

class SimpleBlocDelegate extends BlocDelegate {
  @override
  void onEvent(Bloc bloc, Object event) {
    super.onEvent(bloc, event);
    print('onEvent:' + '$event');
  }

  @override
  void onTransition(Bloc bloc, Transition transition) {
    super.onTransition(bloc, transition);
    print('onTransition:' + '$transition');
  }

  @override
  void onError(Bloc bloc, Object error, StackTrace stacktrace) {
    super.onError(bloc, error, stacktrace);
    print('onError:' + error);
  }
}

void main() {
  BlocSupervisor.delegate = SimpleBlocDelegate();

  runApp(MultiBlocProvider(providers: [
    BlocProvider<LocaleBloc>(
      create: (_) => LocaleBloc()..add(LocaleInit()),
    ),
    BlocProvider<AdBloc>(
      create: (_) => AdBloc()..add(AdStart(5)),
    )
  ], child: EletecApp()));
}
