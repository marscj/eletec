import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:eletec/rest/client.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:wakelock/wakelock.dart';

part 'app_event.dart';
part 'app_state.dart';

class AppBloc extends Bloc<AppEvent, AppState> {
  
  final BuildContext context;

  GlobalKey<OverlayState> overlayKey = GlobalKey();

  OverlayEntry overlayEntry;

  AppBloc(this.context);
  
  @override
  AppState get initialState => AppState.initial();

  @override
  Stream<AppState> mapEventToState(
    AppEvent event,
  ) async* {
    if(event is AppInitial) {

      // 电源管理
      await Wakelock.enable();

      // 强制竖屏
      await SystemChrome.setPreferredOrientations([
        DeviceOrientation.portraitUp,
        DeviceOrientation.portraitDown
      ]);

      // 获取token
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

      // 获取language
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
