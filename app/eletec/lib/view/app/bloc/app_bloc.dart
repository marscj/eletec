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
      yield state.copyWith(tag: 'caonima1');
      yield state.copyWith(tag: 'caonima2');
      yield state.copyWith(tag: 'caonima3');

      yield await CacheService.instance.getToken().then((token) {
        if (token == 'unknow') {
          return state.copyWith(
            hasToken: false
          );
        } else {
          return state.copyWith(
            hasToken: true
          );
        }
      });
    }
  }
}
