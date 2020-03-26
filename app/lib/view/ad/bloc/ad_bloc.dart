import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';

part 'ad_event.dart';
part 'ad_state.dart';

class AdBloc extends Bloc<AdEvent, AdState> {
  @override
  AdState get initialState => AdInitial();

  @override
  Stream<AdState> mapEventToState(
    AdEvent event,
  ) async* {
    // TODO: implement mapEventToState
  }
}
