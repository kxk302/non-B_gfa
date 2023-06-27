#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args) < 2) {
  stop("Specify the logistic regression input file, and the model summary output file", call.=FALSE)
}

inputFile = args[1]
outputFile = args[2]

data <- read.csv(inputFile)
model <- glm(formula=novel_label ~ GQ_count + MR_count + STR_count + APR_count + IR_count + DR_count + Z_count, family="binomial", data=data)

# Save the model summary to file
sink(outputFile)
print(summary(model))
sink()
