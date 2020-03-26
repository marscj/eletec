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
    print(state);
    print(state.timer);
    print(event);
    if (event is AdStart) {
      yield AdRunning(event.timer);
      timerController = RangeStream(event.timer, 0)
          .delay(Duration(milliseconds: 200))
          .interval(Duration(seconds: 1))
          .doOnDone(() => add(AdFinish()))
          .listen((i) => add(AdTimer(i)));
    }

    if (event is AdTimer) {
      yield AdRunning(event.timer);
    }

    if (event is AdFinish) {
      yield AdEnd(0);
    }
  }

  @override
  Future<void> close() {
    timerController.close();
    return super.close();
  }
}
