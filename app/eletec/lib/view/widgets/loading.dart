
import 'package:flutter/cupertino.dart';

class LoadingWidget extends StatelessWidget {
 
  @override
  Widget build(BuildContext context) {
    return CupertinoPopupSurface(
      child: CupertinoActivityIndicator(),
    );
  }
}