import 'package:flutter_bloc/flutter_bloc.dart';

import 'view/app/app.dart';

void main() {
  BlocProvider<AppBloc>(
    create: (context) => AppBloc(context)..add(AppInitial()),
    child: BlocBuilder<AppBloc, AppState>(
      builder: (context, state) => EletecApp(state)
    )
  );
}