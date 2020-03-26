import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:eletec/repository/language.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';

part 'locale_event.dart';
part 'locale_state.dart';

class LocaleBloc extends Bloc<LocaleEvent, LocaleState> {
  @override
  LocaleState get initialState => LocaleState(Locale('en', ''));

  @override
  Stream<LocaleState> mapEventToState(
    LocaleEvent event,
  ) async* {
    if (event is LocaleInit) {
      var lan = await LanguageRepository().get();
      Locale locale = Locale(lan, '');
      yield LocaleState(locale);
    }

    if (event is LocaleUpdate) {
      Locale _locale = event.locale;

      await LanguageRepository().set(event.locale.languageCode);

      yield LocaleState(_locale);
    }
  }
}