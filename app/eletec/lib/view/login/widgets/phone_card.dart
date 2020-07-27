import 'package:eletec/plugs/flutter_form_builder/flutter_form_builder.dart';
import 'package:flutter/material.dart';

class PhoneNumberCard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    
    final form = FormBuilder(
      child: Form(
        child: Column(
          children: <Widget>[

          ],
        ),
      ),
    );

    return FittedBox(
      child: Card(
        child: form,
      ),
    );
  }
  
}