USE [DwidioBak]
GO

/****** Object:  Table [dbo].[aws-billing]    Script Date: 11/2/2017 1:31:45 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[aws-billing](
	[InvoiceID] [varchar](50) NULL,
	[PayerAccountId] [varchar](50) NULL,
	[LinkedAccountId] [varchar](50) NULL,
	[RecordType] [varchar](50) NULL,
	[RecordId] [varchar](50) NULL,
	[ProductName] [varchar](50) NULL,
	[RateId] [varchar](50) NULL,
	[SubscriptionId] [varchar](50) NULL,
	[PricingPlanId] [varchar](50) NULL,
	[UsageType] [varchar](50) NULL,
	[Operation] [varchar](50) NULL,
	[AvailabilityZone] [varchar](50) NULL,
	[ReservedInstance] [varchar](50) NULL,
	[ItemDescription] [varchar](2048) NULL,
	[UsageStartDate] [varchar](128) NULL,
	[UsageEndDate] [varchar](128) NULL,
	[UsageQuantity] [varchar](128) NULL,
	[BlendedRate] [varchar](50) NULL,
	[BlendedCost] [varchar](50) NULL,
	[UnBlendedRate] [varchar](50) NULL,
	[UnBlendedCost] [varchar](50) NULL,
	[ResourceId] [varchar](2048) NULL,
	[aws_autoscaling_groupName] [varchar](512) NULL,
	[user Syncbak Application] [varchar](1024) NULL,
	[user Syncbak Environment] [varchar](1024) NULL,
	[user Syncbak Owner] [varchar](1024) NULL,
	[user Syncbak Role] [varchar](1024) NULL,
	[user syncbak-customer] [varchar](1024) NULL
) ON [PRIMARY]

GO




SELECT
   *
FROM
   [dbo].[aws-billing]
where
   ItemDescription like '%GB data transfer out (Canada)"' or
   ItemDescription like '%GB data transfer out (United States)"' or
   ItemDescription like '%GB data transfer out (Europe)"' or
   ItemDescription like '%GB - next 40 TB / month data transfer out"' or
   ItemDescription like '%GB - next 100 TB / month data transfer out"' or
   ItemDescription like '%GB - next 150 TB / month data transfer out"' or
   ItemDescription like '%GB - greater than 150 TB / month data transfer out"' or
   ItemDescription like '%GB - first 10 TB / month data transfer out beyond the global free tier"' or
   ItemDescription like '%GB - first 50 TB / month of storage used"' or
   ItemDescription like '%GB - next 450 TB / month of storage used"'

SELECT
   UnBlendedCost
FROM
   [dbo].[aws-billing]

SELECT
   UnBlendedCost,
  cast(replace(UnBlendedCost, '"', '') as decimal(10,3)),
   *
   --sum(cast(replace(UnBlendedCost, '"', '') as decimal(10,3)))
FROM
   [dbo].[aws-billing]
