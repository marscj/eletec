import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '../view.dart';

part 'loading_event.dart';
part 'loading_state.dart';

class LoadingBloc extends Bloc<LoadingEvent, LoadingState> {

  GlobalKey<OverlayState> overlayKey = GlobalKey();
  OverlayEntry overlayEntry;
  
  @override
  LoadingState get initialState => LoadingState.initial();

  @override
  Stream<LoadingState> mapEventToState(
    LoadingEvent event,
  ) async* {
    if (event is ShowLoading) {
      yield LoadingState.showDialog();

      overlayEntry ??= OverlayEntry(
        builder: (_) =>  GestureDetector(
          behavior: HitTestBehavior.translucent,
          onTap: () {
            add(DismissLoading());
          },
          child: Container(
            color: Colors.black45, 
            child: CupertinoActivityIndicator(radius: 12)
          )
        )
      );

      overlayKey.currentState.insert(overlayEntry);
    }

    if (event is DismissLoading) {
      yield LoadingState.dismissDialog();
      overlayEntry?.remove();
      overlayEntry = null;
    }
  }
}
