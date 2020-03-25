import 'package:eletec/api/reponse.dart';

class BaseState {}
class LoadingState extends BaseState{}
class SuccessState<T> extends BaseState{
  final Response<T> result;
  SuccessState(this.result);
}
class ErrorState extends BaseState{}
class NoItemState extends BaseState{}