import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';

part 'user_login_event.dart';
part 'user_login_state.dart';

class UserLoginBloc extends Bloc<UserLoginEvent, UserLoginState> {
  @override
  UserLoginState get initialState => UserLoginInitial();

  @override
  Stream<UserLoginState> mapEventToState(
    UserLoginEvent event,
  ) async* {
    // TODO: implement mapEventToState
  }
}
