import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:equatable/equatable.dart';

part 'email_login_event.dart';
part 'email_login_state.dart';

class EmailLoginBloc extends Bloc<EmailLoginEvent, EmailLoginState> {
  @override
  EmailLoginState get initialState => EmailLoginInitial();

  @override
  Stream<EmailLoginState> mapEventToState(
    EmailLoginEvent event,
  ) async* {
    // TODO: implement mapEventToState
  }
}
