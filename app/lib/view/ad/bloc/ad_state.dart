part of 'ad_bloc.dart';

abstract class AdState extends Equatable {
  const AdState();
}

class AdInitial extends AdState {
  @override
  List<Object> get props => [];
}
