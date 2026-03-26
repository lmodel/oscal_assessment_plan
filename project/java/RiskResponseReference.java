package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Identifies an individual risk response that this log entry is for.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskResponseReference  {

  private String response-uuid;
  private List<RelatedTask> related-tasks;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}