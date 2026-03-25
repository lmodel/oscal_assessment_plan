package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Identifies an individual risk response that occurred as part of managing an identified risk.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskLogEntry  {

  private String uuid;
  private String title;
  private String description;
  private ZonedDateTime start;
  private ZonedDateTime end;
  private List<LoggedBy> logged-by;
  private String status-change;
  private List<RiskResponseReference> related-responses;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}