FROM public.ecr.aws/lambda/python:3.12

COPY ../requirements.txt ./
RUN python3.12 -m pip install -r requirements.txt -t .

COPY ten_piece ./ten_piece/

# Command can be overwritten by providing a different command in the template directly.
CMD ["ten_piece.app.lambda_handler"]
