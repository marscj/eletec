import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:eletec/rest/client.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';

part 'app_event.dart';
part 'app_state.dart';

class AppBloc extends Bloc<AppEvent, AppState> {
  
  @override
  AppState get initialState => AppState.initial();

  @override
  Stream<AppState> mapEventToState(
    AppEvent event,
  ) async* {
    if(event is AppInitial) {
      yield await CacheService.instance.getToken().then((token) {
        if (token == 'unknow') {
          return state.copyWith(
            signedIn: false,
          );
        } else {
          return state.copyWith(
            signedIn: true,
          );
        }
      });

      yield await CacheService.instance.getLanguage().then((value) {
        return state.copyWith(
          locale: Locale(value, '')
        );
      });

    }

    if (event is LocaleUpdate) {
      yield state.copyWith(
        locale: Locale(event.languageCode, '')
      );

      CacheService.instance.setLanguage(event.languageCode);
    }

    if (event is SignedIn) {
      yield state.copyWith(
        signedIn: true
      );
      CacheService.instance.setToken(event.token);
    }

    if (event is SignedOut) {
      yield state.copyWith(
        signedIn: false
      );
      CacheService.instance.clearToken();
    }
  }
}
