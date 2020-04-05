part of 'loading_bloc.dart';

abstract class LoadingEvent extends Equatable {
  const LoadingEvent();

  @override
  List<Object> get props => [];
}

class ShowLoading extends LoadingEvent {}

class DismissLoading extends LoadingEvent {}
