import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';
import 'package:rxdart/rxdart.dart';

part 'ad_event.dart';
part 'ad_state.dart';

class AdBloc extends Bloc<AdEvent, AdState> {
  StreamSubscription<int> timerController;

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
        .listen((i) => add(AdEvent(i)));
  }

  @override
  Future<void> close() {
    timerController?.cancel();
    return super.close();
  }
}
