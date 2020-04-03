import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:eletec/rest/client.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';

part 'app_event.dart';
part 'app_state.dart';

class AppBloc extends Bloc<AppEvent, AppState> {
  
  final BuildContext context;

  GlobalKey<OverlayState> overlayKey = GlobalKey();

  AppBloc(this.context);
  
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

    if (event is ShowLoading) {
      OverlayEntry overlayEntry = OverlayEntry(
        builder: (_) =>   Positioned(
          top: MediaQuery.of(context).size.height * 0.5,
          child: new Material(
            child: new Container(
              color: Colors.transparent,
              alignment: Alignment.center,

              child: new Center(
                child: new Container(
                  child: new Padding(
                    padding: EdgeInsets.all(20),
                    child: new Text('message'), 
                  ),
                  color: Colors.grey.withAlpha(128),
                )
              )
            )
          ))
      );

      overlayKey.currentState.insert(overlayEntry);
      new Future.delayed(Duration(seconds: 2)).then((value) {
        overlayEntry.remove();
      });
    }
  }
}
