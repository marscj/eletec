import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';

part 'phone_login_event.dart';
part 'phone_login_state.dart';

class PhoneLoginBloc extends Bloc<PhoneLoginEvent, PhoneLoginState> {
  @override
  PhoneLoginState get initialState => PhoneLoginInitial();

  @override
  Stream<PhoneLoginState> mapEventToState(
    PhoneLoginEvent event,
  ) async* {
    // TODO: implement mapEventToState
  }
}
