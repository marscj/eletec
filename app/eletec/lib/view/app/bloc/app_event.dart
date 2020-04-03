part of 'app_bloc.dart';

abstract class AppEvent extends Equatable {
  const AppEvent();

  @override
  List<Object> get props => [];
}

class AppInitial extends AppEvent {}

class LocaleUpdate extends AppEvent {
  final String languageCode;

  LocaleUpdate(this.languageCode);

  @override
  List<Object> get props => [languageCode];
}

class SignedIn extends AppEvent {
  final String token;

  SignedIn(this.token);

  @override
  List<Object> get props => [token];
}

class SignedOut extends AppEvent {}

class ShowLoading extends AppEvent {}

class DismissLoading extends AppEvent {}