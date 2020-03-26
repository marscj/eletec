import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:rxdart/rxdart.dart';
import 'package:rxdart/subjects.dart';

part 'ad_event.dart';
part 'ad_state.dart';

class AdBloc extends Bloc<AdEvent, AdState> {
  var timerController;

  @override
  AdState get initialState => AdInitial(5);

  @override
  Stream<AdState> mapEventToState(
    AdEvent event,
  ) async* {
    if (event is AdStart) {
      yield AdRunning(state.timer);

      timerController = Stream.fromIterable([5, 4, 3, 2, 1])
          .delay(Duration(milliseconds: 200))
          .interval(Duration(seconds: 1))
          .doOnDone(() => print('finsh'))
          .listen((i) => add(AdTimer(i)));
    }
  }

  @override
  Future<void> close() {
    timerController.close();
    return super.close();
  }
}
