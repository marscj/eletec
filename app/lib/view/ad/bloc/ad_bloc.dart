import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:eletec/config/router.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';
import 'package:rxdart/rxdart.dart';

part 'ad_event.dart';
part 'ad_state.dart';

class AdBloc extends Bloc<AdEvent, AdState> {

  final BuildContext context;
  
  StreamSubscription<int> timerController;

  AdBloc(this.context);

  @override
  AdState get initialState => AdState(5);

  @override
  Stream<AdState> mapEventToState(
    AdEvent event,
  ) async* {
    yield AdState(event.timer);
    timerController ??= RangeStream(4, 0)
        .delay(Duration(seconds: 1))
        .interval(Duration(seconds: 1))
        .doOnDone(() {
          Router.instance.navigateTo(context, '/home', replace: true);
        })
        .listen((i) => add(AdEvent(i)));
  }

  @override
  Future<void> close() {
    timerController?.cancel();
    return super.close();
  }
}
