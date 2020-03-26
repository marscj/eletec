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
  AdState get initialState => AdState(5);

  @override
  Stream<AdState> mapEventToState(
    AdEvent event,
  ) async* {
    yield AdState(event.timer);
    timerController = RangeStream(4, 0)
        .delay(Duration(seconds: 1))
        .interval(Duration(seconds: 1))
        .listen((i) => add(AdEvent(i)));
  }

  @override
  Future<void> close() {
    timerController.close();
    return super.close();
  }
}
